FROM public.ecr.aws/lambda/python:3.10

# Install system dependencies
RUN yum install -y gcc postgresql-devel

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy function code
COPY lambda_function.py .

# Command to run the Lambda function
CMD ["lambda_function.lambda_handler"]