class Track
  constructor: (@event, @timeRanges) ->
    @length = @timeRanges.length
    @first = @timeRanges[0]
    @last = @timeRanges[@length - 1]

  search: (time, L) ->
    return @search(time, @timeRanges) if not L?
    return -1 if L.length == 0
    mid = Math.floor(L.length / 2)
    if L[mid].contains(time)
      return mid
    else if L[mid].isBefore(time)
      return @search(val, L[(mid + 1)..L.length])
    else
      return @search(val, L[0..(mid - 1)])