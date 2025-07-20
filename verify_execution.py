#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wavelength Field Theory - Execution Verification Script
======================================================

This script verifies that all Python scripts can run successfully
and produce the expected corrected results.

Author: Oliver Jay Hooton
Email: oliver.j.hooton@gmail.com
Date: 2025-01-20
"""

import os
import sys
import subprocess
import pandas as pd
import numpy as np

def check_python_version():
    """Check Python version is 3.13+"""
    print("🔍 Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 13:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Need 3.13+")
        return False

def check_packages():
    """Check required packages are installed"""
    print("\n🔍 Checking required packages...")
    required_packages = ['numpy', 'scipy', 'matplotlib', 'sympy', 'pandas']
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} - OK")
        except ImportError:
            print(f"❌ {package} - Missing")
            return False
    return True

def check_scripts_exist():
    """Check all Python scripts exist"""
    print("\n🔍 Checking script files...")
    scripts = [
        'src/wavelength_field_validation.py',
        'src/theoretical_foundations.py',
        'src/comprehensive_critique_solutions.py',
        'src/fundamental_derivations_response.py',
        'src/enhanced_manuscript_improvements.py'
    ]
    
    for script in scripts:
        if os.path.exists(script):
            print(f"✅ {script} - Found")
        else:
            print(f"❌ {script} - Missing")
            return False
    return True

def run_script(script_name, timeout=300):
    """Run a Python script and return success status"""
    try:
        print(f"\n🚀 Running {script_name}...")
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=os.getcwd()
        )
        
        if result.returncode == 0:
            print(f"✅ {script_name} - SUCCESS")
            return True
        else:
            print(f"❌ {script_name} - FAILED")
            print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"❌ {script_name} - TIMEOUT")
        return False
    except Exception as e:
        print(f"❌ {script_name} - ERROR: {e}")
        return False

def verify_corrected_results():
    """Verify the corrected parameter values are present"""
    print("\n🔍 Verifying corrected results...")
    
    try:
        # Check fundamental derivations results
        df = pd.read_csv('results/fundamental_derivations_results.csv')
        
        # Check key corrected values
        expected_values = {
            'g1_Constraint': 3.16e-07,
            'g2_Constraint': 3.16e-08,
            'alpha1_Constraint': 3.16e-06,
            'alpha2_Constraint': 3.16e-08,
            'Mercury_Perihelion_WFT': 2.14e-170,
            'Light_Deflection_WFT': 6.02e-168,
            'GW_Speed_Correction': 1e-70
        }
        
        for param, expected in expected_values.items():
            if param in df['Parameter'].values:
                actual = df[df['Parameter'] == param]['Value'].iloc[0]
                if abs(actual - expected) < 1e-10:
                    print(f"✅ {param} = {actual:.2e} - CORRECT")
                else:
                    print(f"❌ {param} = {actual:.2e} (expected {expected:.2e})")
                    return False
            else:
                print(f"❌ {param} - Missing from results")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading results: {e}")
        return False

def check_output_files():
    """Check that expected output files are generated"""
    print("\n🔍 Checking output files...")
    
    expected_files = [
        'results/complete_30_test_validation_results.csv',
        'results/theoretical_foundations_results.csv',
        'results/comprehensive_critique_results.csv',
        'results/fundamental_derivations_results.csv',
        'results/enhanced_manuscript_results.csv',
        'figures/parameter_constraints_comprehensive.png',
        'figures/detailed_cosmological_predictions.png',
        'figures/comprehensive_theoretical_diagrams.png',
        'figures/complete_cosmological_evolution.png',
        'figures/generalized_em_fractions.png',
        'figures/enhanced_manuscript_analysis.png'
    ]
    
    all_exist = True
    for file_path in expected_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} - Found")
        else:
            print(f"❌ {file_path} - Missing")
            all_exist = False
    
    return all_exist

def main():
    """Main verification function"""
    print("=" * 60)
    print("WAVELENGTH FIELD THEORY - EXECUTION VERIFICATION")
    print("=" * 60)
    
    # Check prerequisites
    if not check_python_version():
        print("\n❌ Python version check failed")
        return False
    
    if not check_packages():
        print("\n❌ Package check failed")
        print("Run: pip install numpy scipy matplotlib sympy pandas")
        return False
    
    if not check_scripts_exist():
        print("\n❌ Script files check failed")
        return False
    
    # Run all scripts
    scripts = [
        'src/wavelength_field_validation.py',
        'src/theoretical_foundations.py',
        'src/comprehensive_critique_solutions.py',
        'src/fundamental_derivations_response.py',
        'src/enhanced_manuscript_improvements.py'
    ]
    
    all_success = True
    for script in scripts:
        if not run_script(script):
            all_success = False
    
    if not all_success:
        print("\n❌ Some scripts failed to run")
        return False
    
    # Verify results
    if not verify_corrected_results():
        print("\n❌ Corrected results verification failed")
        return False
    
    if not check_output_files():
        print("\n❌ Output files check failed")
        return False
    
    # Success summary
    print("\n" + "=" * 60)
    print("✅ ALL VERIFICATIONS PASSED!")
    print("=" * 60)
    print("\n🎉 EXECUTION VERIFICATION COMPLETE")
    print("✅ All scripts run successfully")
    print("✅ All corrected results verified")
    print("✅ All output files generated")
    print("✅ Ready for other users to reproduce results")
    
    print("\n📋 SUMMARY:")
    print("• Python version: ✅ Compatible")
    print("• Required packages: ✅ Installed")
    print("• Script files: ✅ Present")
    print("• Script execution: ✅ Successful")
    print("• Corrected results: ✅ Verified")
    print("• Output files: ✅ Generated")
    
    print("\n🚀 READY FOR DISTRIBUTION!")
    print("Other users can now run the scripts and reproduce all results.")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 