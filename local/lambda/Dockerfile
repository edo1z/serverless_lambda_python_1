FROM amazon/aws-sam-cli-build-image-python3.8

WORKDIR /app

RUN curl -fsSL https://rpm.nodesource.com/setup_17.x | bash -
RUN yum install -y nodejs
RUN pip install awscli boto3
RUN npm install -g npm
RUN npm install -g serverless serverless-offline serverless-dotenv-plugin

CMD ["/bin/bash"]