# How I labelled (written before the agent existed)

- Not a call for papers (a sponsor appeal, an unconference with no advance submission): `is_cfp` false, name null, deadline and date null, every enum `unclear`.
- `submission_deadline`: the one date by which a speaker must submit. If the posting gives no date, only a relative one ("six weeks before"), a rolling close, a numeric date that could be day-first or month-first, or two deadlines with no clear final one, it is null. If a deadline is extended, the new date is the deadline. A date with no year takes its year from the "Posted" line.
- `format`: `hybrid` if the posting says both an in-person and an online way to take part; a posting that only names a venue is `in_person`.
- `audience_level`: one value. "Beginners and experts" or "all levels" is `all`. A range like "intermediate and advanced" takes the lower one.
- `travel_support`: `full` flights and lodging both covered; `partial` something covered, or capped, or conditional for all speakers; `none` stated that nothing is paid, or the event is online, or aid exists only for a narrow group; `unclear` not stated, or left to the organisers' discretion.
