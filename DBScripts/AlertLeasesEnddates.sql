select 
	propertyname
	,u.unitaddress
	,DATEDIFF(day,  l.enddate,getdate()) days_left_on_lease
	,getdate() + 90 as COMMERCIAL_ENDDATE_THRESSHOLD
	,l.enddate
 
from leases l 
inner join units u on l.unit = u.unitid
inner join properties p on p.propertyid = u.PropertyID
where l.status = 'ACTIVE' and (enddate >= getdate() and enddate <= GETDATE() + 90) and p.propertyclass = 'COMMERCIAL';

select
	propertyname 
	,u.unitaddress
	,DATEDIFF(day,  l.enddate, GETDATE()) days_left_on_lease
	,getdate() + 30 as RESIDENTIAL_ENDDATE_THRESSHOLD
	,l.enddate
from leases l 
inner join units u on l.unit = u.unitid
inner join properties p on p.propertyid = u.PropertyID
where l.status = 'ACTIVE' and (enddate >= getdate() and enddate <= GETDATE() + 30) and p.propertyclass = 'RESIDENTIAL';