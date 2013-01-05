randrange = (a, b) ->
  randval = a + (Math.random()*(b - a))
  Math.round randval

describe "ExecutedTrack", ->
  beforeEach ->
    window.spy = jasmine.createSpy('eventFn')
    window.event = new CueEvent 5, "Hello world!"
    window.track = new window.ExecutedTrack new window.Track(window.spy, [event])

  it "runs correctly with a playheadTime equal to the first CueEvent", ->
   window.track.execute 5
   expect(window.spy).toHaveBeenCalled()

  it "runs correctly with a playheadTime less than the first CueEvent time", ->
    window.track.execute 2
    expect(window.spy).not.toHaveBeenCalled()

  it "runs correctly with a playheadTime for a random position in the Track", ->
    window.track.execute randrange 1, 100
    expect(window.spy).not.toHaveBeenCalled()

  it "runs correctly with a playheadTime right after the last CueEvent", ->
    window.track.execute 6
    expect(window.spy).not.toHaveBeenCalled()
