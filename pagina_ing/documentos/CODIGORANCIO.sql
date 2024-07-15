DECLARE 
    CURSOR cursor_empleados (
        p_id_vacunatorio NUMBER
    ) IS
    SELECT
        nombre_emp,
        appaterno_emp,
        numrun_emp,
        round(months_between(sysdate, fecing_emp) / 12) AS "anio",
        sueldo_base_emp
        
    FROM
        empleado
    WHERE
        id_vacunatorio = p_id_vacunatorio;

    CURSOR cursor_vacunatorio IS
    SELECT
        id_vacunatorio as vacunatorios
    FROM
        vacunatorio;
BEGIN
    FOR registro_empleados IN cursor_empleados(10) LOOP
        dbms_output.put_line('RUN: ' || registro_empleados.numrun_emp);
        FOR registro_vacunatorio IN cursor_vacunatorio LOOP
            dbms_output.put_line('ID VACUNATORIO: ' || registro_vacunatorio.vacunatorios);
        END LOOP;
    END LOOP;
END;
