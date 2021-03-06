FROM python
COPY . ./app
WORKDIR ./app
RUN pip install -r requirements.txt
EXPOSE 7735
CMD python app.py
