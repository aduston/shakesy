randrange = (a, b) ->
  randval = a + (Math.random()*(b - a))
  Math.round randval

describe "ExecutedTrack", ->
  beforeEach ->
    window.spy = jasmine.createSpy('eventFn')
    window.track = new window.ExecutedTrack new window.Track(window.spy, [new window.CueEvent(5,'World')])
    spyOn(spy)

  it "Runs correctly with a playheadTime less than the first CueEvent time", ->
    window.track.execute 9
    expect(window.spy).toHaveBeenCalled()

  it "Runs correctly with a playheadTime for a random position in the Track", ->
    window.track.execute randrange 1, 100
    expect(window.spy).toHaveBeenCalled()

  it "Runs correctly with a playheadTime right after the last CueEvent", ->
    window.track.execute 6
    expect(window.spy).toHaveBeenCalled()


