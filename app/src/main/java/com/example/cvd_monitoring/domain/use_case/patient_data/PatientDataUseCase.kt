package com.example.cvd_monitoring.domain.use_case.patient_data

import com.example.cvd_monitoring.domain.model.users.CreateUserRequest
import com.example.cvd_monitoring.domain.model.users.PatientData
import com.example.cvd_monitoring.domain.model.users.User
import com.example.cvd_monitoring.domain.repository.PatientRepository
import javax.inject.Inject

class PatientDataUseCase @Inject constructor(
    private val patientRepository: PatientRepository
){
    suspend operator fun invoke(patient: PatientData, slug: String): PatientData {
        return patientRepository.updatePatientData(patient, slug)
    }
}