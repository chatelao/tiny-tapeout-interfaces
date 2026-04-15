# REST API Tests

## Batch Simulation
Request:
POST /simulation
{
  "target": "tt08",
  "inputs": [
    {
      "ui_in": 85,
      "uio_in": 0,
      "ena": true,
      "rst_n": true,
      "clock": "0"
    },
    {
      "ui_in": 170,
      "uio_in": 0,
      "ena": true,
      "rst_n": true,
      "clock": "1"
    }
  ]
}

Response:
200 OK
{
  "target": "tt08",
  "outputs": [
    {
      "uo_out": 85,
      "uio_out": 0,
      "uio_oe": 0
    },
    {
      "uo_out": 170,
      "uio_out": 0,
      "uio_oe": 0
    }
  ]
}

## Random Target Simulation
Request:
POST /simulation
{
  "inputs": [
    {
      "ui_in": 0,
      "uio_in": 0,
      "ena": true,
      "rst_n": true,
      "clock": "01"
    }
  ]
}

Response:
200 OK

## Simulation with Flash PMOD contents
Request:
POST /simulation
{
  "target": "tt08",
  "flash": "SGVsbG8gV29ybGQ=",
  "inputs": [
    {
      "ui_in": 0,
      "uio_in": 0,
      "ena": true,
      "rst_n": true
    }
  ]
}

Response:
200 OK
{
  "target": "tt08",
  "flash": "SGVsbG8gV29ybGQ=",
  "outputs": [
    {
      "uo_out": 0,
      "uio_out": 0,
      "uio_oe": 0
    }
  ]
}

## Simulation with Repeat
Request:
POST /simulation
{
  "target": "tt08",
  "inputs": [
    {
      "ui_in": 123,
      "repeat": 3
    }
  ]
}

Response:
200 OK
{
  "target": "tt08",
  "outputs": [
    {
      "uo_out": 123,
      "uio_out": 0,
      "uio_oe": 0
    },
    {
      "uo_out": 123,
      "uio_out": 0,
      "uio_oe": 0
    },
    {
      "uo_out": 123,
      "uio_out": 0,
      "uio_oe": 0
    }
  ]
}

## Create Session
Request:
POST /sessions
{
  "tt-delivers": "tt08",
  "address": 10
}

Response:
201 Created
{
  "session_id": "DYNAMIC"
}

## Session Simulation
Request:
POST /sessions/{session_id}/simulation
{
  "inputs": [
    {
      "ui_in": 42
    }
  ]
}

Response:
200 OK
{
  "target": "tt08",
  "address": 10,
  "outputs": [
    {
      "uo_out": 42,
      "uio_out": 0,
      "uio_oe": 0
    }
  ]
}

## Session Set Signals
Request:
POST /sessions/{session_id}/set
{
  "ui_in": 99
}

Response:
200 OK
{
  "uo_out": 99,
  "uio_out": 0,
  "uio_oe": 0
}

## Session Reset
Request:
POST /sessions/{session_id}/reset
{}

Response:
204 No Content

## Create Session with Flash
Request:
POST /sessions
{
  "tt-delivers": "tt08",
  "address": 20,
  "flash": "SGVsbG8gV29ybGQ="
}

Response:
201 Created
{
  "session_id": "DYNAMIC"
}

## Session Simulation with Pre-initialized Flash
Request:
POST /sessions/{session_id}/simulation
{
  "inputs": [
    {
      "ui_in": 10
    }
  ]
}

Response:
200 OK
{
  "target": "tt08",
  "address": 20,
  "flash": "SGVsbG8gV29ybGQ=",
  "outputs": [
    {
      "uo_out": 10,
      "uio_out": 0,
      "uio_oe": 0
    }
  ]
}
