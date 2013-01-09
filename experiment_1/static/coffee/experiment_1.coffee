$("script").first().before($('<script/>').attr('src', '//www.youtube.com/iframe_api'))

window.onYouTubeIframeAPIReady = () ->
  $("#player").eventedVideo({ tracks: getTracks() })

getTracks = () ->
  eventFn = (data) -> $
  cueEvents = (new CueEvent(s["start_time"], s["text"]) for s in SUBS)
  console.log cueEvents
  [new Track(eventFn, cueEvents)]
