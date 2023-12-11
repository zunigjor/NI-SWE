# HW6 - Web Annotations

### Solution:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Course Information</title>
</head>
<body>

<div itemscope itemtype="http://example.org/Course">
  At our university we offer
  <span itemprop="name">Semantic Web and Knowledge Graphs</span>
  course that has
  <span itemprop="credits">5</span> credits.
  <a href="http://dojchinovski.mk" itemprop="lecturer">Milan Dojčinovski</a>
  lectures in this course every
  <span itemprop="day">Tuesday</span>
  from
  <span itemprop="startTime">11:00</span>
  to
  <span itemprop="endTime">12:30</span>
  in the
  <span itemprop="location">National Library of Technology</span>
  in
  <span itemprop="room">TK:PU1</span>.
</div>

<div xmlns:ex="http://example.org/" typeof="ex:Course">
  At our university we offer
  <span property="ex:name">Semantic Web and Knowledge Graphs</span>
  course that has
  <span property="ex:credits">5</span> credits.
  <a href="http://dojchinovski.mk/" property="ex:lecturer" typeof="ex:Person"><span property="ex:name">Milan Dojčinovski</span></a>
  lectures in this course every
  <span property="ex:timeLocation" typeof="ex:Event">
    <span property="ex:day">Tuesday</span>
    from
    <span property="ex:startTime">11:00</span>
    to
    <span property="ex:endTime">12:30</span>
    in the
    <span property="ex:location" typeof="ex:Place">National Library of Technology</span>
    in
    <span property="ex:room">TK:PU1</span>.
  </span>
</div>

</body>
</html>

```