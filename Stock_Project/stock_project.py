import apache_beam as beam
import yfinance as yf
import sqlalchemy
import pandas as pd
from apache_beam.options.pipeline_options import PipelineOptions
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.time_sensor import TimeSensor
from airflow.sensors.weekday import DayOfWeekSensor
#has some errors

dburl='mysql+pymysql://root:8551649@localhost:3306/stock_data'
engine = sqlalchemy.create_engine(dburl)

ticker='WFC'

class getData(beam.DoFn): # getData class inhernc from beam.DoFn
    def process(self,ticker): # check date for getting new data
        now=datetime.now()
        dataQuery='SELECT MAX(Date) FROM wfc'
        newData=pd.read_sql(dataQuery,engine).value[0][0]
        if newData is None:
            newData='2024-01-02'
        
        stock_data=yf.download(ticker,start=newData,end=now)
        for Date, row in stock_data.iterrows(): #format data to 3 decimal plays
            yield{
                'symbol':ticker,
                'Date':Date,
                'Open':round(row['Open'],3),
                'High':round(row['High'],3),
                'Low':round(row['Low'],3),
                'Close':round(row['Close'],3),
                'Adj Close':round(row['Adj Close'],3),
                'Volume':row['Volume']
            }

class storeData(beam.DoFn):
    def start_bundle(self):
        self.engine=sqlalchemy.create_engine(dburl)

    def process(self, ticker):
        data = pd.DataFrame([ticker])
        data.to_sql(ticker, self.engine, if_exists='append', index=False)

    def finish_bundle(self):
        pass # no cleanup needed for SQLAlchemy engine

def runPipeline():
    options=PipelineOptions() # create pipeline options
    with beam.Pipeline(options=options) as p:
        (p
         |'Create' >> beam.Create([ticker])
         |'Get data' >> beam.ParDo(getData())
         |'Store to MySQL' >> beam.ParDo(storeData())
        )
# airflow dag, dictionary type conainer, MAP in C++       
args={
    'owner':'airflow',
    'depends_past':False,
    'start': datetime(2024,1,2),
    'retries':1,
    'delay':timedelta(minutes=5)
}

dag=DAG(
    'stockData',
    default_args=args,
    description='Get stock data and store in MySQL',
    schedule_interval='*/10 9-16* *1-5', #run the dag every 10 minute from 9-16, Monday to Friday
    catchup=False # do not catchup
)

start=TimeSensor(
    task='wait until market open',
    target_time=datetime.time(9, 30),#9:30 am
    mode='reschedule',
    dag=dag,
)
end=TimeSensor(
    task='wait until market close',
    target_time=datetime.time(16, 0), #4:00 pm
    mode='reschedule',
    dag=dag,
)

weekday=DayOfWeekSensor(
    task='check weekday',
    week_day='Monday,Tuesday,Wednesday,Thursday,Friday',
    use_task_execution_day=True,
    mode='reschedule',
    dag=dag
)
run=PythonOperator(
    task='run etl',
    python_callable=runPipeline,
    dag=dag
)
start>>weekday>>run>>end
