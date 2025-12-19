USE secure_dbaas;

INSERT INTO healthcare
(first_name, last_name, gender, age, weight, height, health_history, integrity_tag)
VALUES
('Alice', 'Smith', X'01', X'19', 65.0, 165.0, 'No major illness', X'00'),
('Bob', 'Jones', X'00', X'20', 80.5, 175.0, 'Diabetes', X'00');
