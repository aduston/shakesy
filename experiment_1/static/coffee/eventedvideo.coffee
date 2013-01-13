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
      if event.data is YT.PlayerState.PLAYING
        @state = setInterval @timerTick_, 50
      else if event.data is YT.PlayerState.PAUSED
        clearInterval(@state)
    tracks: (tracks) ->
      @executedTracks = (new ExecutedTrack(t) for t in tracks)
    timerTick_: () =>
      time = @player.getCurrentTime()
      (t.execute(time) for t in @executedTracks)

  $.fn.eventedVideo = (option) ->
    this.each () ->
      $this = $(this)
      data = $this.data(DATA_KEY)
      $this.data(DATA_KEY, data = new EventedVideo(this)[key](data) for key, data of option) if not data?

  window.EventedVideo = EventedVideo
  )(window.jQuery)


