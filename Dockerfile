FROM python:3.9-slim
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} jupyter \
    && useradd -m -u ${UID} -g ${GID} jupyter

WORKDIR /home/jupyter
ENV PATH="$PATH:/home/jupyter/.local/bin"
USER jupyter
COPY requirements.txt .
RUN python3 -m pip install \
    --no-cache-dir --disable-pip-version-check \
    -r requirements.txt

EXPOSE 8888
CMD ["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0"]
