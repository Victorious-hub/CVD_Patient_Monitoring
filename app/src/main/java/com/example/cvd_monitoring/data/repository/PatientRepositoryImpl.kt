package com.example.cvd_monitoring.data.repository

import com.example.cvd_monitoring.data.CvdApi
import com.example.cvd_monitoring.data.models.PatientDto
import com.example.cvd_monitoring.domain.model.users.Auth
import com.example.cvd_monitoring.domain.model.users.CreateUserRequest
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
}