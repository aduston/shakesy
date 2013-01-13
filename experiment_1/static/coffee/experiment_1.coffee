$("script").first().before($('<script/>').attr('src', '//www.youtube.com/iframe_api'))

window.onYouTubeIframeAPIReady = () ->
  $("#player").eventedVideo({ tracks: getTracks() })

getTracks = () ->
  eventFn = (data) -> displaySubtitle(data)
  cueEvents = (new CueEvent(s["start_time"] / 10.0, s["text"]) for s in SUBS)
  [new Track(eventFn, cueEvents)]

displaySubtitle = (sub) ->
  $('#subtitle').text(sub ? '')
