package com.example.cvd_monitoring.domain.use_case.sign_sup

import com.example.cvd_monitoring.domain.model.users.CreateUserRequest
import com.example.cvd_monitoring.domain.model.users.User
import com.example.cvd_monitoring.domain.repository.PatientRepository
import javax.inject.Inject

class CreatePatientUseCase @Inject constructor (
    private val patientRepository: PatientRepository
) {
    suspend operator fun invoke(firstName: String, lastName: String, email: String, password: String): User {
        val user = User(firstName, lastName, email, password)
        val createUserRequest = CreateUserRequest(user)
        return patientRepository.createPatient(createUserRequest)
    }
}