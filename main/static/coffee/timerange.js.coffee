class TimeRange
  constructor: (@startTime, @endTime, @data) ->
  contains: (playheadTime) ->
    @startTime <= playheadTime && playheadTime < @endTime
  isAfter: (playheadTime) ->
    @startTime > playheadTime
  isBefore: (playheadTime) ->
    @endTime <= playheadTime
  startsBefore: (playheadTime) ->
    @startTime <= playheadTime
  startsAfter: (playheadTime) ->
    @startTime > playheadTime
