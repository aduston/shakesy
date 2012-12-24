class Track
  constructor: (@eventFn_, cueEvents) ->
    cueEvents.sort (a, b) -> a.time - b.time
    if cueEvents[0].time > 0
      @cueEvents = [new CueEvent(0)].concat(cueEvents)
    else
      @cueEvents = cueEvents

  search: (time, L) ->
    return @search(time, @cueEvents) if not L?
    throw new Error("time not found") if L.length == 0
    mid = Math.floor(L.length / 2)
    event = L[mid]
    nextEvent = L[mid + 1]
    if event.startTime <= time && (!nextEvent || nextEvent.startTime > time)
      mid
    else if event.startTime <= time
      @search(val, L[(mid + 1)..L.length])
    else
      @search(val, L[0..(mid - 1)])

  eventHasTime: (index, time) ->
    event = @curEvents[index]
    nextEvent = @curEvents[index + 1]
    event && event.time <= time && (!nextEvent || nextEvent.time > time)

  execute: (index) ->
    @eventFn_(@cueEvents[index])