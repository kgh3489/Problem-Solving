

SELECT MCDP_CD 진료과코드, count(*) 5월예약건수
from APPOINTMENT
where Year(APNT_YMD) = 2022 and month(APNT_YMD) = 5
group by MCDP_CD
order by count(*), MCDP_CD