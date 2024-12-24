#1001, Alice, Math, 85
#1002, Bob, Math, 78
#1001, Alice, English, 92
#1002, Bob, English, 88

put 'student_scores','1001-Math', 'info:name','Alice'
put 'student_scores','1001-Math', 'info:score','85'
put 'student_scores','1002-Math', 'info:name','Bob'
put 'student_scores','1002-Math', 'info:score','78'
put 'student_scores','1001-English', 'info:name','Alice'
put 'student_scores','1001-English', 'info:score','92'
put 'student_scores','1002-English', 'info:name','Bob'
put 'student_scores','1002-English', 'info:score','88'

put 'student_scores','0606-Math', 'info:name','Chenyu'
put 'student_scores','0606-Math', 'info:score','150'
put 'student_scores','0606-English', 'info:name','Chenyu'
put 'student_scores','0606-English', 'info:score','420'

put 'student_scores','0601-Math', 'info:name','1111'
put 'student_scores','0601-Math', 'info:score','99'

deleteall 'student_scores','0601-Math'
scan 'student_scores', {FILTER => "RowFilter(=, 'regexstring:.*-Math$')", COLUMNS => ['info:score', 'info:name']}
# scan 'student_scores', {FILTER => "RowFilter(=, 'regexstring:.*-Math$')", COLUMNS => ['info:score', 'info:name'],REVERSED => true}
# scan 'student_scores', {COLUMN => 'info:score', FILTER => "SingleColumnValueFilter('info', 'subject', =, 'binary:Math') AND RowFilter(=, 'binary:Math')", REVERSED => true}
# scan 'student_scores', {COLUMN => 'info:score', FILTER => "SingleColumnValueFilter('info', 'subject', =, 'binary:Math') AND SingleColumnValueFilter('info', 'score', >, '0')", ORDER_BY => 'info:score', REVERSED => true}
# scan 'student_scores', {FILTER => "RowFilter(=, 'regexstring:.*-Math$')", COLUMNS => ['info:score', 'info:name'], REVERSED => true}
# scan 'student_scores', {FILTER => "RowFilter(=, 'regexstring:.*-Math$')", COLUMNS => ['info:score', 'info:name'], REVERSED => true}
# scan 'student_scores', {FILTER => "RowFilter(=, 'regexstring:.*-Math$')", COLUMNS => ['info:score', 'info:name'], SORT => 'info:score', REVERSED => true}
