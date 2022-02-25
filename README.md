# Data channel server

This example illustrates establishing a data channel with a
browser. It also performs some image processing on the video frames using
OpenCV.

## Running

First install the required packages:

.. code-block:: console

    $ pip install aiohttp aiortc opencv-python

When you start the example, it will create an HTTP server which you
can connect to from your browser:

.. code-block:: console

    $ python server.py
