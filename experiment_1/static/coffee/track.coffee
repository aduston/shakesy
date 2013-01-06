class Track
  constructor: (@eventFn_, cueEvents) ->
    cueEvents.sort (a, b) -> a.time - b.time
    if cueEvents[0].time > 0
      @cueEvents = [new window.CueEvent(0)].concat(cueEvents)
    else
      @cueEvents = cueEvents
      
  search: (time, L) ->
    return @search(time, @cueEvents) if not L?
    throw new Error("time not found") if L.length == 0
    low = 0
    high = L.length - 1
    while low <= high
      mid = Math.floor (low + high) / 2
      if time < L[mid].time
        high = mid - 1
      else if @eventHasTime mid, time
        return mid
      else
        low = mid + 1
    return -1

  eventHasTime: (index, time) ->
    event = @cueEvents[index]
    nextEvent = @cueEvents[index + 1]
    console.log nextEvent
    console.log !nextEvent
    console.log nextEvent.time > time if nextEvent
    event && event.time <= time && (!nextEvent || nextEvent.time > time)

  execute: (index) ->
    @eventFn_(@cueEvents[index].data)

window.Track = Track
