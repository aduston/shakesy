$("script").first().before($('<script/>').attr('src', '//www.youtube.com/iframe_api'))

window.onYouTubeIframeAPIReady = () ->
  $("#player").eventedVideo({ tracks: getTracks() })

getTracks = () ->
  eventFn = (data) -> console.log(data)
  cueEvents = (new CueEvent(s["start_time"], s["data"]) for s in SUBS)
  [new Track(eventFn, cueEvents)]
