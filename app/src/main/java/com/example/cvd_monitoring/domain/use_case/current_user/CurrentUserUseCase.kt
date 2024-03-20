package com.example.cvd_monitoring.domain.use_case.current_user

import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.domain.repository.PatientRepository
import javax.inject.Inject

class CurrentUserUseCase @Inject constructor(
    private val patientRepository: PatientRepository
){
    suspend operator fun invoke(slug: String): Patient{
        return patientRepository.getCurrentUser(slug)
    }
}