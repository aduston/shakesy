DATA_KEY = 'eventedVideo'

!(($) ->
  class EventedVideo
    constructor: (@elem) ->
      @$elem = $(@elem)
      @player = new YT.Player(
        @elem.id,
        events:
          'onReady': (e) => @onPlayerReady_(e)
          'onStateChange': (e) => @onPlayerStateChange_(e))
    onPlayerReady_: (event) ->
      console.log(event)
    onPlayerStateChange_: (event) ->
      console.log(event)
    tracks: (tracks) ->
      @executedTracks = (new ExecutedTrack(t) for t in tracks)
    timerTick_: (playheadTime) ->
      (t.execute(playheadTime) for t in @executedTracks)

  $.fn.eventedVideo = (option) ->
    this.each () ->
      $this = $(this)
      data = $this.data(DATA_KEY)
      $this.data(DATA_KEY, data = new EventedVideo(this)) if not data?
  )(window.jQuery)

window.EventedVideo = EventedVideo
