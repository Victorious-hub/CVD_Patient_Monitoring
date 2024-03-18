package com.example.cvd_monitoring.domain.use_case.patient_list

import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.domain.repository.PatientRepository
import javax.inject.Inject

class GetPatientListUseCase @Inject constructor (
    private val patientRepository: PatientRepository
) {
    suspend operator fun invoke(): List<Patient> {
        return patientRepository.getPatients()
    }

}