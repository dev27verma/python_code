Pyspark Setup for Pycharm
Download Jdk 17.0.2
Dowload Python 3.10
Download Pycharm-community version
Dowload git
Download spark-3.5.6-bin-hadoop3
Download winutils.exe    from https://github.com/steveloughran/winutils/tree/master/hadoop-3.0.0/bin
Under C:\Program Files create two folder: 
    spark-3.5.6: Paste all files under spark-3.5.6-bin-hadoop3 to spark-3.5.6
    hadoop: create bin folder under hadoop and paste winutils.exe
Environment Variable:
  variable name: JAVA_HOME
  variable value: C:\Program Files\Java\jdk-17
  variable name: HADOOP_HOME
  variable value: C:\Program Files\hadoop
  variable name: SPARK_HOME
  variable value: C:\Program Files\spark-3.5.6
  variable name: PYSPARK_DRIVER_PYTHON
  variable value: python
  variable name: PYSPARK_PYTHON
  variable value: python
Under PATH:
  C:\Users\Devendra\AppData\Local\Programs\Python\Python310\
  C:\Users\Devendra\AppData\Local\Programs\Python\Python310\Scripts\
  %JAVA_HOME%\bin
  %HADOOP_HOME%\bin
  %SPARK_HOME%\bin
  %SPARK_HOME%\python
  C:\Program Files\spark-3.5.6\python\lib\py4j-0.10.9.7-src.zip
  C:\Program Files\Git\bin\
  C:\Program Files\Git\cmd\
Make two root folder: go to setting in pycharm --> project --> project_structure --> add_content_root --> select below files
  C:\Program Files\spark-3.5.6\python\lib\py4j-0.10.9.7-src
  C:\Program Files\spark-3.5.6\python\lib\pyspark
  
