# REST API Tests

## Get Pin State
Request:
GET /pins

Response:
200 OK
{
  "ui_in": 0,
  "uo_out": 0,
  "uio": 0
}

## Set Pin State
Request:
PUT /pins/ui_in
{
  "state": 1
}

Response:
200 OK
