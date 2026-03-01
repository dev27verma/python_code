merge into table1 as A
using table2 as B on (a.emp_id=b.emp_id)
when matched then
	update set a.emp_name=b.emp_name
when not matched then
	insert(emp_id, emp_name)
	values(b.emp_id, b.emp_name)