From python:3.7
COPY . /market_analysis
WORKDIR /market_analysis
EXPOSE 7000
RUN pip install -r requirements.txt
RUN pytest -c tests/test_scripts.py
CMD ["python", "app/api.py"]
