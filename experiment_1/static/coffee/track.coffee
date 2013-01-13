class Track
  constructor: (@eventFn_, cueEvents) ->
    cueEvents.sort (a, b) -> a.time - b.time
    if cueEvents[0].time > 0
      @cueEvents = [new window.CueEvent(0)].concat(cueEvents)
    else
      @cueEvents = cueEvents
      
  search: (time) ->
    low = 0
    high = @cueEvents.length - 1
    while low <= high
      mid = Math.floor (low + high) / 2
      if time < @cueEvents[mid].time
        high = mid - 1
      else if @eventHasTime mid, time
        return mid
      else
        low = mid + 1
    return -1

  eventHasTime: (index, time) ->
    event = @cueEvents[index]
    nextEvent = @cueEvents[index + 1]
    event && event.time <= time && (!nextEvent || nextEvent.time > time)

  execute: (index) ->
    @eventFn_(@cueEvents[index].data)

window.Track = Track
