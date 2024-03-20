package com.example.cvd_monitoring.data.repository

import com.example.cvd_monitoring.data.CvdApi
import com.example.cvd_monitoring.domain.model.users.Auth
import com.example.cvd_monitoring.domain.model.users.CreateUserRequest
import com.example.cvd_monitoring.domain.model.users.DoctorContact
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.domain.model.users.PatientContact
import com.example.cvd_monitoring.domain.model.users.PatientData
import com.example.cvd_monitoring.domain.model.users.User
import com.example.cvd_monitoring.domain.repository.PatientRepository
import javax.inject.Inject

class PatientRepositoryImpl @Inject constructor(
    private val api: CvdApi
) : PatientRepository {
    override suspend fun authenticateUser(auth: Auth): Auth {
        return api.authenticateUser(auth)
    }

    override suspend fun createPatient(patient: CreateUserRequest): User {
        return api.createPatient(patient)
    }

    override suspend fun getPatients(): List<Patient> {
        return api.getPatients()
    }

    override suspend fun getCurrentUser(slug: String): Patient {
        return api.getCurrentUser(slug)
    }

    override suspend fun updateDoctorContact(doctor: DoctorContact, slug: String): DoctorContact {
        return api.updateDoctorContact(doctor, slug)
    }

    override suspend fun updatePatientContact(patient: PatientContact, slug: String): PatientContact {
        return api.updatePatientContact(patient, slug)
    }

    override suspend fun updatePatientData(patient: PatientData, slug: String): PatientData {
        return api.updatePatientData(patient, slug)
    }

}