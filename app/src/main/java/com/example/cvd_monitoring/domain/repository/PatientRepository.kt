package com.example.cvd_monitoring.domain.repository

import com.example.cvd_monitoring.data.models.PatientDto
import com.example.cvd_monitoring.domain.model.users.Auth
import com.example.cvd_monitoring.domain.model.users.CreateUserRequest
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.domain.model.users.PatientContact
import com.example.cvd_monitoring.domain.model.users.PatientData
import com.example.cvd_monitoring.domain.model.users.User
import retrofit2.http.Body

interface PatientRepository {
    suspend fun authenticateUser(@Body auth: Auth): Auth

    suspend fun createPatient(@Body patient: CreateUserRequest): User

    suspend fun updatePatientData(@Body patient: PatientData, slug: String): PatientData

    suspend fun getPatients(): List<Patient>

    suspend fun updatePatientContact(@Body patient: PatientContact, slug: String): PatientContact
}