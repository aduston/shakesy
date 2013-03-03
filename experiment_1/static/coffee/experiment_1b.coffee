$("script").first().before($('<script/>').attr('src', '//www.youtube.com/iframe_api'))

window.onYouTubeIframeAPIReady = () ->
  $("#player").eventedVideo({ tracks: getTracks() })

getTracks = () ->
  eventFn = displaySubtitleData
  cueEvents = (new CueEvent(s["start_time"] / 10.0, s) for s in SUBS)
  [new Track(eventFn, cueEvents)]

displaySubtitleData = (data) ->
  $('.subtitle').toggle(data?)
  $('#character').toggle(data?)
  $('.subtitle.original').html(if data then data['original_text'].replace(/\n/g, '<br/>') else '')
  $('.subtitle.contemporary').text(if data then data['contemporary_text'] else '')
  if data?
    character = CHARACTERS[data['character_id'] + '']
    $('#character .photo').attr('src', character['image']) if character['image']
    $('#character .photo').toggle(!!character['image'])
    $('#character .name').text(character['name'])
    $('#character .title').text(character['title'])
