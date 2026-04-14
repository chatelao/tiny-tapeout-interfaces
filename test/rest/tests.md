# REST API Tests

## Batch testing
Request:
POST /simulation
{
  "target": "tt08",
  "address": 1,
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
  "address": 1,
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

## Random Target testing
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

## testing with Flash PMOD contents
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
  "address": 0,
  "flash": "SGVsbG8gV29ybGQ=",
  "outputs": [
    {
      "uo_out": 0,
      "uio_out": 0,
      "uio_oe": 0
    }
  ]
}
