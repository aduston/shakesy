class ExecutedTrack
  constructor: (@track) ->
    @curIndex_ = -1
  execute: (playheadTime) ->
    if @curIndex_ == -1
      @executeNoCurIndex_(playheadTime)
    else if @track.eventHasTime(@curIndex_, playheadTime)
      return
    else if @track.eventHasTime(@curIndex_ + 1, playheadTime)
      @executeCurIndex_(curIndex_ + 1)
    else
      @executeNoCurIndex_(playheadTime)
  executeNoCurIndex_: (playheadTime) ->
    @executeCurIndex_(@track.search(playheadTime))
  executeCurIndex_: (curIndex) ->
    if curIndex != @curIndex_
      @track.execute(@curIndex_ = curIndex)
window.ExecutedTrack = ExecutedTrack

