randrange = (a, b) ->
  randval = a + (Math.random()*(b - a))
  Math.round randval

describe "ExecutedTrack", ->
  spy = null
  track = null
  
  beforeEach ->
    spy = jasmine.createSpy('eventFn')
    events = [new CueEvent(1.2, "a"), new CueEvent(2.6, "b")]
    track = new window.ExecutedTrack new window.Track(spy, events)

  it "runs correctly with a playheadTime equal to the first CueEvent", ->
    track.execute 1.2
    expect(spy).toHaveBeenCalledWith("a")

  it "runs correctly with a playheadTime less than the first CueEvent time", ->
    track.execute 1
    expect(spy).toHaveBeenCalledWith(null or undefined)

  it "runs correctly with a playheadTime for a position between two CueEvents", ->
    track.execute 2
    expect(spy).toHaveBeenCalledWith("a")

  it "runs correctly with a playheadTime right after the last CueEvent", ->
    track.execute 3
    expect(spy).toHaveBeenCalledWith("b")
