$("script").first().before($('<script/>').attr('src', '//www.youtube.com/iframe_api'))

subContainer = $('.scrolling-sidebar')
sideSubs = {}
curSub = null

makeSub = (s, lastSub) ->
  sub = $('<div>')
  if not lastSub? or lastSub['character_id'] != s['character_id']
    character = CHARACTERS[s['character_id'] + '']
    sub.append($('<h5>').text(character['name'])) if character?
  sub.append($('<p>').html(s['original_text'].replace(/\n/g, '<br/>')))
  sub.click ->
    $('#player').eventedVideo({ setPlayhead: s['start_time'] / 10.0})
    displaySubtitleData(s)
  sub

addSubsToRight = () ->
  lastSub = null
  for s in SUBS
    sub = makeSub(s, lastSub)
    sideSubs[s['start_time']] = sub
    subContainer.append(sub)
    lastSub = s

addSubsToRight()

window.onYouTubeIframeAPIReady = () ->
  $("#player").eventedVideo({ tracks: getTracks() })

getTracks = () ->
  eventFn = displaySubtitleData
  cueEvents = (new CueEvent(s["start_time"] / 10.0, s) for s in SUBS)
  [new Track(eventFn, cueEvents)]

displaySubtitleData = (data) ->
  $('.scrolling-sidebar .current').removeClass('current')
  if data?
    sub = sideSubs[data['start_time']]
    curSub = sub
    offsetTop = sub.get(0).offsetTop
    $('.scrolling-sidebar').animate(
      scrollTop: offsetTop - 240 + sub.height() / 2,
      200,
      () -> sub.addClass('current') if sub == curSub)
    $('#video_overlay .subtitle').show().html(data['contemporary_text'].replace(/\n/g, '<br/>'))
  else
    $('#video_overlay .subtitle').hide()