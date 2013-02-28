$("script").first().before($('<script/>').attr('src', '//www.youtube.com/iframe_api'))

window.onYouTubeIframeAPIReady = () ->
  $("#player").eventedVideo({ tracks: getTracks() })

getTracks = () ->
  eventFn = displaySubtitleData
  cueEvents = (new CueEvent(s["start_time"] / 10.0, s) for s in SUBS)
  [new Track(eventFn, cueEvents)]

displaySubtitleData = (data) ->
  $('.subtitle').toggle(data?)
  $('.subtitle.original').html(if data then data['original_text'].replace('\n', '<br/>') else '')
  $('.subtitle.contemporary').text(if data then data['contemporary_text'] else '')
#  $('.characters .cur-character').removeClass('cur-character')
#  $("[data-charid=#{data['character_id']}]").addClass('cur-character') if data
