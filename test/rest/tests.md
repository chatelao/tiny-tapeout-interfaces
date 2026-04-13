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
      "rst_n": true
    },
    {
      "ui_in": 170,
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
      "rst_n": true
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
