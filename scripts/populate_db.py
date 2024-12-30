import random
from datetime import datetime, timedelta
import psycopg2
from faker import Faker
from tqdm import tqdm

fake = Faker(['ru_RU'])

DB_PARAMS = {
    "dbname": "medical_system",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

SPECIALIZATIONS = [
    "Терапевт", "Кардиолог", "Невролог", "Офтальмолог", 
    "Хирург", "Педиатр", "Эндокринолог", "Гастроэнтеролог",
    "Дерматолог", "Отоларинголог"
]

SOCIAL_STATUSES = [
    "Работающий", "Пенсионер", "Студент", "Безработный",
    "Инвалид", "Военнослужащий", "Предприниматель"
]

CONDITIONS = [
    "Стабильное", "Улучшение", "Ухудшение", 
    "Выздоровление", "Требует наблюдения"
]

DIAGNOSES = [
    "Гипертоническая болезнь", "ОРВИ", "Бронхит",
    "Гастрит", "Артрит", "Мигрень", "Диабет 2 типа",
    "Остеохондроз", "Аллергический ринит", "Пневмония",
    "Депрессия", "Астма", "Язва желудка"
]

def generate_patients(num_patients):
    return [
        (
            fake.name(),
            random.randint(1940, 2005),
            random.choice(SOCIAL_STATUSES)
        )
        for _ in range(num_patients)
    ]

def generate_doctors(num_doctors):
    return [
        (
            fake.name(),
            random.choice(SPECIALIZATIONS),
            random.randint(1, 40)  
        )
        for _ in range(num_doctors)
    ]

def generate_treatments(patient_ids, doctor_ids, num_treatments):
    """Generate treatment data"""
    treatments = []
    
    for _ in range(num_treatments):
        start_date = fake.date_between(start_date='-2y', end_date='today')
        
        if random.random() > 0.3:
            end_date = start_date + timedelta(days=random.randint(5, 180))
        else:
            end_date = None
            
        treatments.append((
            random.choice(patient_ids),
            random.choice(doctor_ids),
            random.choice(DIAGNOSES),
            start_date,
            end_date,
            random.choice(CONDITIONS)
        ))
    
    return treatments

def populate_database():
    """Main function to populate the database"""
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    
    try:
        print("Generating patients...")
        patients = generate_patients(1000)
        
        print("Generating doctors...")
        doctors = generate_doctors(50)
        
        print("Inserting patients...")
        patient_ids = []
        for patient in tqdm(patients):
            cur.execute(
                """
                INSERT INTO patient (fio, year_of_birth, social_status)
                VALUES (%s, %s, %s) RETURNING patient_id
                """,
                patient
            )
            patient_ids.append(cur.fetchone()[0])
        
        print("Inserting doctors...")
        doctor_ids = []
        for doctor in tqdm(doctors):
            cur.execute(
                """
                INSERT INTO doctor (fio, specialization, experience)
                VALUES (%s, %s, %s) RETURNING doctor_id
                """,
                doctor
            )
            doctor_ids.append(cur.fetchone()[0])
        
        print("Generating treatments...")
        treatments = generate_treatments(patient_ids, doctor_ids, 2000)
        
        print("Inserting treatments...")
        for treatment in tqdm(treatments):
            cur.execute(
                """
                INSERT INTO treatment 
                (patient_id, doctor_id, diagnosis, start_date, end_date, current_condition)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                treatment
            )
        
        conn.commit()
        print("Database population completed successfully!")
        
        cur.execute("SELECT COUNT(*) FROM patient")
        patient_count = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM doctor")
        doctor_count = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM treatment")
        treatment_count = cur.fetchone()[0]
        
        print(f"\nStatistics:")
        print(f"Patients inserted: {patient_count}")
        print(f"Doctors inserted: {doctor_count}")
        print(f"Treatments inserted: {treatment_count}")
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {str(e)}")
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    populate_database()

