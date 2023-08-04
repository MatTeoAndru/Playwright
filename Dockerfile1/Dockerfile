#https://www.lambdatest.com/learning-hub/playwright-docker
#https://www.digitalocean.com/community/tutorials/how-to-run-end-to-end-tests-using-playwright-and-docker
# https://github.com/microsoft/playwright-dotnet/issues/2058

FROM mcr.microsoft.com/playwright/python:v1.35.0-jammy



ENV PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright


WORKDIR /app

COPY requirementsPW.txt /app

COPY ./testOk /app


RUN  pip install  --upgrade pip \
  && pip install  -r requirementsPW.txt

#RUN PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright python -m playwright install

RUN apt-get update && playwright install-deps 

EXPOSE 8000



CMD ["/bin/bash"]