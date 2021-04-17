FROM python
RUN pip install pymysql cryptography
COPY ./docker/python/rds.py /
CMD [ "python", "/rds.py" ]