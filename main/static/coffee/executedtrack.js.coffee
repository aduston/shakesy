class ExecutedTrack
  constructor: (@track) ->
    @curIndex_ = -1
  curTimeRange_ = () ->
    @track.timeRanges[@curIndex_]
  execute: (playheadTime) ->
    if @curIndex_ != -1 && !@curTimeRange_().contains(playheadTime)
      @track.event(@curTimeRange_().data, false)
    return @executeNoCurIndex_(playheadTime) if @curIndex_ == -1
    nextTimeRange = @track.timeRanges[@curIndex_ + 1]
    return if @curTimeRange_().startsBefore(playheadTime) &&
      (!nextTimeRange || nextTimeRange.startsAfter(playheadTime))
    if nextTimeRange && nextTimeRange.contains(playheadTime)
      @curIndex_ += 1
      @track.event(@curTimeRange_().data, true)
    else
      @executeNoCurIndex_(playheadTime)
  executeNoCurIndex_: (playheadTime) ->
    if playheadTime >= @track.first.startTime && playheadTime <= @track.last.endTime
      @curIndex_ = @track.search(playheadTime)
      @track.event(@curTimeRange_().data, true) if @curIndex_ != -1
    else
      @curIndex_ = -1
