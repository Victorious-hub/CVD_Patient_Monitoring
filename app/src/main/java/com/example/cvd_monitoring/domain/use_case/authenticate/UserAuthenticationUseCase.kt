package com.example.cvd_monitoring.domain.use_case.authenticate

import com.example.cvd_monitoring.domain.model.users.Auth
import com.example.cvd_monitoring.domain.repository.PatientRepository
import javax.inject.Inject

class UserAuthenticationUseCase @Inject constructor(
    private val patientRepository: PatientRepository
) {
    suspend operator fun invoke(email: String, password: String): Auth {
        val auth = Auth(email, password)
        return patientRepository.authenticateUser(auth)
    }
}