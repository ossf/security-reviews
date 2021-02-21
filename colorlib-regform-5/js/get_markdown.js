Date.prototype.toDateInputValue = (function() {
        var local = new Date(this);
        local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
        return local.toJSON().slice(0,10);
    });

    $(window).on('load', function() {
        $('#reviewDate').val(new Date().toDateInputValue());

        $('.copyClipboard').on('click', function(e) {
            $('#markdown').select();
            const result = document.execCommand('copy');
            if (!result) {
                alert('Unable to copy to clipboard. Press Ctrl-C instead.');
            } else {
                $("#markdown").blur();
            }
        });

        $('#packageURLs').on('keyup', function() {
            $('#packageURLs')[0].setCustomValidity('');
            $('#packageURLs')[0].reportValidity();
        });

        $('form').on('submit', function(e) {

            e.preventDefault();

            var t = '';
            t += '---\n'
            t += 'Publication-State: ' + $('#publicationState').val() + '\n';

            t += 'Access: ' + $('#access').val() + '\n';
            t += 'Reviewers:\n';

            var prefix = '-';
            if ($('#reviewer0Name').val()) t += prefix + ' Name: ' + $('#reviewer0Name').val() + '\n'; prefix = ' ';
            if ($('#reviewer0Email').val()) t += prefix + ' Email: ' + $('#reviewer0Email').val() + '\n'; prefix = ' ';
            if ($('#reviewer0Organization').val()) t += prefix + ' Organization: ' + $('#reviewer0Organization').val() + '\n';
            if ($('#reviewer0AssociatedWithProject').val()) t += '  Associated-With-Project: ' + $('#reviewer0AssociatedWithProject').val() + '\n';
            if ($('#reviewer0CompensationSource').val()) t += '  Compensation-Source: ' + $('#reviewer0CompensationSource').val() + '\n';

            t += 'Domain: ' + $('#domain').val() + '\n';

            t += 'Methodology:\n';
            if ($('#staticAnalysis').is(':checked')) t += '- Static-Analysis\n';
            if ($('#dynamicAnalysis').is(':checked')) t += '- Dynamic-Analysis\n';
            if ($('#webSearch').is(':checked')) t += '- Web-Search\n';
            if ($('#codeReview').is(':checked')) t += '- Code-Review\n';
            if ($('#externalReview').is(':checked')) t += '- External-Review\n';
            if ($('#fuzzing').is(':checked')) t += '- Fuzzing\n';

            t += 'Issues-Identified: ' + $('#issuesIdentified').val() + '\n';

            t += 'Package-URLs:\n';
            var abortSubmission = false;
            $.each($('#packageURLs').val().split("\n"), (idx, url) => {
                if (url !== '' && !url.startsWith('pkg:')) {
                    $('#packageURLs')[0].setCustomValidity('Each line must contain a valid PackageURL.');
                    $('#packageURLs')[0].reportValidity();
                    abortSubmission = true;
                    return false;
                }
                if (url !== '') {
                    t += '- ' + url.trim() + '\n';
                }
            });

            t += 'Review-Date: ' + $('#reviewDate').val() + '\n';
            t += 'Scope: ' + $('#scope').val() + '\n';
            t += 'Schema-Version: ' + $('#schemaVersion').val() + '\n';
            t += 'SPDX-License-Identifier: ' + $('#spdxLicense').val() + '\n';
            t += '---\n\n';

            t += '### Summary\n\n';
            t += $('#summary').val().trim() + '\n\n';

            t += '### Details\n\n';
            t += $('#details').val().trim() + '\n\n';

            t += '### Methodology\n\n';
            t += $('#methodology').val().trim() + '\n\n';

            t += '### External References\n\n';
            const refs = $('#externalReferences').val().trim();
            if (refs !== '') {
                t += $('#externalReferences').val().trim() + '\n\n';
            } else {
                t += 'No external references were provided.\n\n';
            }

            t += '### Disclaimer\n\n';
            t += 'All security reviews are conducted on a "best-effort" basis against a software\n';
            t += 'component at a point in time. We make no guarantee as to the quality or completeness\n';
            t += 'of any review. If you believe any content is inaccurate, we encourage you to open\n';
            t += 'an issue or submit a pull request with a correction or improvement.\n\n';

            t += '### License\n\n';
            t += 'This text is released under at least the\n';
            t += '[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).\n';
            t += 'Externally-referenced content may be licensed differently.\n';

            alert(t);

            $('#markdown').val(t);
            $('.modal').modal();
        });
    });
