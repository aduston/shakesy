randrange = (a, b) ->
  randval = a + (Math.random()*(b - a))
  Math.round randval

describe "ExecutedTrack", ->
  spy = null
  track = null
  executed_track = null
  
  beforeEach ->
    spy = jasmine.createSpy('eventFn')
    events = [new CueEvent(1.2, "a"), new CueEvent(2.6, "b")]
    track = new window.Track(spy, events)
    executed_track = new window.ExecutedTrack track

  it "runs correctly with a playheadTime equal to the first CueEvent", ->
    executed_track.execute 1.2
    expect(spy).toHaveBeenCalledWith("a")

  it "runs correctly with a playheadTime less than the first CueEvent time", ->
    executed_track.execute 1
    expect(spy).toHaveBeenCalledWith(null or undefined)

  it "runs correctly with a playheadTime for a position between two CueEvents", ->
    executed_track.execute 2
    expect(spy).toHaveBeenCalledWith("a")

  it "runs correctly with a playheadTime right after the last CueEvent", ->
    executed_track.execute 3
    expect(spy).toHaveBeenCalledWith("b")

  it "does not execute a second time when a new playhead time is given for the same cue event", ->
    executed_track.execute 1.4
    executed_track.execute 1.5
    expect(spy.calls.length).toEqual(1)

  it "does not invoke a binary search twice when a new playhead time is given for the same cue event", ->
    spyOn(track, 'search').andCallThrough()
    executed_track.execute 1.4
    executed_track.execute 1.5
    expect(track.search.calls.length).toEqual(1)

  it "does not invoke a binary search twice when a new playhead time is given for the next cue event", ->
    spyOn(track, 'search').andCallThrough()
    executed_track.execute 1.4
    executed_track.execute 2.7
    expect(track.search.calls.length).toEqual(1)
