# base image
FROM public.ecr.aws/lambda/python:3.10

# we need to install tf-lite and other dependencies
# lambda will create the env on its own and also install other
# dependencies like numpy which are needed by tf-lite and keras-image-helper
# however we needed here specific version of numpy to get stuff working
RUN pip install numpy==1.24.1
RUN pip install keras-image-helper

# This tflite runs into some missing libs on AWS linux
# so we choose another tf-lite package already compiles on AWS ERC
# RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

# copy pipfiles in current dir (i.e. app dir)
COPY clothing-model.tflite .
COPY lambda_function.py .

# Specify how to find the lambda function handler
CMD ["lambda_function.lambda_handler"]